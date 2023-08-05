import requests

urls = [
    "../static/css/anime_min.css",
    "../static/css/episode_min.css",
    "../static/css/episode_min.css",
    "../static/css/search_min.css",
    "https://cdn.jsdelivr.net/gh/epic-designer/AnimeDex@main/static/css/video_min.css",
]


for url in urls:
    url = url[24:]
    r = requests.get("https://purge.jsdelivr.net" + url)
    print(r.json().get("status"), url)
