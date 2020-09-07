import boto3

def modify_vpn_tunnel_options_batch(client, key, value):
    response = client.modify_vpn_tunnel_options(
        VpnConnectionId=key,
        VpnTunnelOutsideIpAddress=value,
        TunnelOptions={
            'Phase1EncryptionAlgorithms': [
                {
                    'Value': 'AES256-GCM-16'
                },
            ],
            'Phase2EncryptionAlgorithms': [
                {
                    'Value': 'AES256-GCM-16'
                },
            ],
            'Phase1IntegrityAlgorithms': [
                {
                    'Value': 'SHA2-256'
                },
            ],
            'Phase2IntegrityAlgorithms': [
                {
                    'Value': 'SHA2-256'
                },
            ],
            'Phase1DHGroupNumbers': [
                {
                    'Value': 18
                },
            ],
            'Phase2DHGroupNumbers': [
                {
                    'Value': 18
                },
            ],
            'IKEVersions': [
                {
                    'Value': 'ikev2'
                },
            ]
        },
        DryRun=True
    )

    print(response)


def main():
    input = {
        "vpn-id": "outside-ip-address"
    }

    client = boto3.client('ec2')

    for key, value in input.items():
        modify_vpn_tunnel_options_batch(client, key, value)


if __name__ == '__main__':
    main()
