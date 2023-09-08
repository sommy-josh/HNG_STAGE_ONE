from django.http import JsonResponse
from datetime import datetime

def get_info(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    current_day = datetime.utcnow().strftime('%A')
    current_utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/username/repo"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data)
