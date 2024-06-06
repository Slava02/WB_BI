## ClickHouse
**Ссылка на DockerHub:** https://hub.docker.com/r/clickhouse/clickhouse-server
```bash
docker run -d --name click --ulimit nofile=262144:262144 clickhouse/clickhouse-server
docker restart clickhouse-server
docker stop clickhouse-server
docker rm clickhouse-server
```

## Grafana
**Ссылка на DockerHub:** https://hub.docker.com/r/grafana/grafana
```bash
docker run -d --name=grafana -p 3000:3000 grafana/grafana
docker restart grafana
docker stop grafana
docker rm grafana 
```
