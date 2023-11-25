# elasticsearch-grafana-alerts
Shows integration of elastic search (as database) with grafana. We define alerts and generated sample data to trigger alerts.



# Setup 
## Run services
```
docker-compose up -d

# go to http://localhost:3000 for grafana
# use admin/admin_password as username and password respectively (NOTE: please be more secure in a prod env)
```

## Add documents to elastic search
``` 
python -m venv E:\venvs\elasticsearch-grafana-alerts # make new virtual env

E:\venvs\elasticsearch-grafana-alerts\Scripts\activate.bat # enable the virtual env
```

# Debugging and development 
```
curl http://localhost:9200 # elastic-search health check

pip freeze > requirements.txt # record python dependencies

```

# ToDo
- why are dashboard not picked up automatically from git? 
- 