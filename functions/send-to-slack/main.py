def send_to_slack(event, context):
    webhook_url = get_secret('slack_webhook')
    cloud_build_message = event.data
    build_status = cloud_build_message.get('attributes').get('status')
    build_id = cloud_build_message.get('attributes').get('buildId')
    if build_status == 'SUCCESS':
        slack_text = f':large_green_circle: Cloud Build Success for {build_id}'
    else:
        slack_text = f':red_circle: ATTENTION! Cloud Build {build_id} did not succeed. Status is {build_status}.'
    slack_message = dict(text=slack_text)
    requests.post(webhook_url, json=slack_message)

    def get_secret(secret_name, version="latest"):
        secret_client = secretmanager.SecretManagerServiceClient()
        secret_path = client.secret_version_path(project, secret_name, version)
        secret = client.access_secret_version(secret_path)
        return secret.payload.data.decode("UTF-8")