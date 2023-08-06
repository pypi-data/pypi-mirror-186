NAMESPACE='teleport'
RELEASE_NAME='teleport'
MYZONE_DNS='aws.araalinetworks.com'
MYDNS='devops.aws.araalinetworks.com'
MY_CLUSTER_REGION='us-west-2'
MYZONE="$(aws route53 list-hosted-zones-by-name --dns-name="${MYZONE_DNS?}" | jq -r '.HostedZones[0].Id' | sed s_/hostedzone/__)"
MYELB="$(kubectl --namespace "${NAMESPACE?}" get "service/${RELEASE_NAME?}" -o jsonpath='{.status.loadBalancer.ingress[*].hostname}')"
MYELB_NAME="${MYELB%%-*}"
MYELB_ZONE="$(aws elbv2 describe-load-balancers --region "${MY_CLUSTER_REGION?}" --names "${MYELB_NAME?}" | jq -r '.LoadBalancers[0].CanonicalHostedZoneId')"
jq -n --arg dns "${MYDNS?}" --arg elb "${MYELB?}" --arg elbz "${MYELB_ZONE?}" \
    '{
        "Comment": "Create records",
        "Changes": [
          {
            "Action": "CREATE",
            "ResourceRecordSet": {
              "Name": $dns,
              "Type": "A",
              "AliasTarget": {
                "HostedZoneId": $elbz,
                "DNSName": ("dualstack." + $elb),
                "EvaluateTargetHealth": false
              }
            }
          },
          {
            "Action": "CREATE",
            "ResourceRecordSet": {
              "Name": ("*." + $dns),
              "Type": "A",
              "AliasTarget": {
                "HostedZoneId": $elbz,
                "DNSName": ("dualstack." + $elb),
                "EvaluateTargetHealth": false
              }
            }
          }
      ]
    }' > myrecords.json
cat myrecords.json | jq
CHANGEID="$(aws route53 change-resource-record-sets --hosted-zone-id "${MYZONE?}" --change-batch file://myrecords.json | jq -r '.ChangeInfo.Id')"
aws route53 get-change --id "${CHANGEID?}" | jq '.ChangeInfo.Status'
