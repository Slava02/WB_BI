#clickhouse

docker run -d \
--name click \
--restart unless-stopped \
--cpus="1.0" \
--memory="1g" \
-p 8123:8123 -p 9000:9000 \
-v ch-storage:/var/lib/clickhouse \
-v ch-logs:/var/log/clickhouse-server/ \
--volume=$(pwd)/docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d/
clickhouse/clickhouse-server


#grafana

docker run -d \
-p 3000:3000 \
--name=grafana \
--restart unless-stopped \
--cpus="1.0" \
--memory="1g" \
--volume grafana-storage:/var/lib/grafana \
-e "GF_INSTALL_PLUGINS=grafana-clock-panel" \
grafana/grafana-enterprise