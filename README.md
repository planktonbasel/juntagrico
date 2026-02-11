# Juntagrico für planktonbasel

See docs at: https://juntagrico.readthedocs.io/en/stable/intro/installation.html

## Development

# 1. Install uv (one-time)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Create virtualenv with auto-downloaded Python (reads .python-version)
uv venv

# 3. Install from requirements.txt into the venv
uv pip install -r requirements.txt

# 4. Run Django (uv detects and uses the .venv automatically)
```
DJANGO_SETTINGS_MODULE=planktonbasel.settings-dev uv run python manage.py migrate
First Time: DJANGO_SETTINGS_MODULE=planktonbasel.settings-dev uv run python -m manage createadmin
DJANGO_SETTINGS_MODULE=planktonbasel.settings-dev uv run python manage.py collectstatic --noinput
DJANGO_SETTINGS_MODULE=planktonbasel.settings-dev uv run python manage.py runserver
```

### Updates

Currently package version are managed as follows:

#### Development
Pin to compatible minor version.
```
juntagrico~=1.7.8
juntagrico-billing~=1.7.6
```

#### Production
Pin to exact minor version. Manually update after testing compatibility.
```
juntagrico==1.7.8
juntagrico-billing==1.7.6
```
## Deployment

### Dockerfile
The Dockerfile is for reference only as the new platform builds its own image

### Juntagrico Managed Hosting
The new hosting platform is managed by Juntagrico.
1. Make sure the Github repository is up to date
2. Login to: https://admin.juntagrico.science
3. Deploy a new version
