LABELS = {
    "rebalance_progress": "Rebalance progress, %",
    "ops": "Ops per sec",
    "cmd_get": "GET ops per sec",
    "cmd_set": "SET ops per sec",
    "delete_hits": "DELETE ops per sec",
    "cas_hits": "CAS ops per sec",
    "curr_connections": "Connections",
    "hibernated_waked": "Streaming requests wakeups per sec",
    "curr_items": "Active items",
    "mem_used": "Memory used, bytes",
    "ep_meta_data_memory": "Metadata in RAM, bytes",
    "vb_active_resident_items_ratio": "Active docs resident, %",
    "vb_replica_resident_items_ratio": "Replica docs resident, %",
    "ep_num_value_ejects": "Ejections per sec",
    "ep_dcp_replica_items_remaining": "DCP replication backlog, items",
    "ep_dcp_replica_total_bytes": "DCP replication bytes sent, bytes",
    "ep_dcp_other_items_remaining": "DCP clients backlog, items",
    "ep_dcp_other_total_bytes": "DCP clients bytes sent, bytes",
    "disk_write_queue": "Disk write queue, items",
    "ep_cache_miss_rate": "Cache miss ratio, %",
    "ep_bg_fetched": "Disk reads per sec",
    "ep_diskqueue_drain": "Drain rate, items/sec",
    "avg_bg_wait_time": "BgFetcher wait time, us",
    "avg_disk_commit_time": "Disk commit time, s",
    "avg_disk_update_time": "Disk update time, us",
    "couch_docs_data_size": "Docs data size, bytes",
    "couch_docs_actual_disk_size": "Docs total disk size, bytes",
    "couch_docs_fragmentation": "Docs fragmentation, %",
    "couch_total_disk_size": "Total disk size, bytes",
    "replication_changes_left": "Outbound XDCR mutations, items",
    "replication_size_rep_queue": "XDC replication queue, bytes",
    "replication_rate_replication": "Mutation replication rate per sec",
    "replication_bandwidth_usage": "Data replication rate, bytes/sec",
    "replication_work_time": "Secs in replicating",
    "replication_commit_time": "Secs in checkpointin",
    "replication_active_vbreps": "Active vbucket replications",
    "replication_waiting_vbreps": "Waiting vbucket replications",
    "replication_num_checkpoints": "Checkpoints issued",
    "replication_num_failedckpts": "Checkpoints failed",
    "replication_meta_latency_wt": "Weighted meta ops latency, ms",
    "replication_docs_latency_wt": "Weighted doc ops latency, ms",
    "xdc_ops": "Total XDCR operations per sec",
    "ep_num_ops_get_meta": "Metadata reads per sec",
    "ep_num_ops_set_meta": "Metadata sets per sec",
    "ep_num_ops_del_meta": "Metadata deletes per sec",
    "couch_views_ops": "View reads per sec",
    "couch_views_data_size": "Views data size, bytes",
    "couch_views_actual_disk_size": "Views total disk size, bytes",
    "couch_views_fragmentation": "Views fragmentation, %",
    "cpu_utilization_rate": "CPU utilization across all cores in cluster, %",
    "swap_used": "Swap space in use across all servers in cluster, bytes",
    "beam.smp_rss": "beam.smp resident set size, bytes",
    "beam.smp_cpu": "beam.smp CPU utilization, %",
    "memcached_rss": "memcached resident set size, bytes",
    "memcached_cpu": "memcached CPU utilization, %",
    "indexer_rss": "indexer resident set size, bytes",
    "indexer_cpu": "indexer CPU utilization, %",
    "projector_rss": "projector resident set size, bytes",
    "projector_cpu": "projector CPU utilization, %",
    "cbq-engine_rss": "query resident set size, bytes",
    "cbq-engine_cpu": "query CPU utilization, %",
    "cbft_rss": "FTS resident set size, bytes",
    "cbft_cpu": "FTS CPU utilization, %",
    "backup_rss": "backup resident set size, bytes",
    "backup_cpu": "backup CPU utilization, %",
    "sync_gateway_rss": "Sync Gateway resident set size, bytes",
    "sync_gateway_cpu": "Sync Gateway CPU utilization, %",
    "xdcr_lag": "Total XDCR lag (from memory to memory), ms",
    "xdcr_persistence_time": "Observe latency, ms",
    "xdcr_diff": "Replication lag, ms",
    "latency_set": "SET ops latency, ms",
    "latency_get": "GET ops latency, ms",
    "latency_query": "Query latency, ms",
    "latency_observe": "OBSERVE latency, ms",
    "latency_persist_to": "persistTo=1 latency, ms",
    "latency_replicate_to": "replicateTo=1 latency, ms",
    "Sys": "Bytes obtained from system",
    "Alloc": "Bytes allocated and still in use",
    "HeapAlloc": "Bytes allocated and still in use",
    "HeapObjects": "Total number of allocated objects",
    "PauseTotalNs": "Total GC pause time, ns",
    "PauseNs": "GC pause time, ns",
    "NumGC": "GC events",
    "PausesPct": "Percentage of total time spent in GC, %",
    "gateway_push": "Single push request to SGW, ms",
    "gateway_pull": "Single pull request to SGW, ms",
    "data_rbps": "Bytes read/sec",
    "data_wbps": "Bytes written/sec",
    "data_avgqusz": "The average queue length",
    "data_util": "Disk bandwidth utilization, %",
    "index_rbps": "Bytes read/sec",
    "index_wbps": "Bytes written/sec",
    "index_avgqusz": "The average queue length",
    "index_util": "Disk bandwidth utilization, %",
    "backup_rbps": "Bytes read/sec",
    "backup_wbps": "Bytes written/sec",
    "backup_avgqusz": "The average queue length",
    "backup_util": "Disk bandwidth utilization, %",
    "bucket_compaction_progress": "Compaction progress, %",
    "in_bytes_per_sec": "Incoming bytes/sec",
    "out_bytes_per_sec": "Outgoing bytes/sec",
    "in_packets_per_sec": "Incoming packets/sec",
    "out_packets_per_sec": "Outgoing packets/sec",
    "ESTABLISHED": "Connections in ESTABLISHED state",
    "TIME_WAIT": "Connections in TIME_WAIT state",
    "index_num_rows_returned": "Number of rows returned by 2i",
    "index_scan_bytes_read": "Bytes read by 2i scans",
    "index_num_requests": "Number of 2i requests",
    "index_num_docs_indexed": "Number of documents indexed in 2i",
    "index_num_docs_pending": "Number of remaining documents to be indexed",
    "index_fragmentation": "fragmentation in secondary indexing",
    "index_data_size": "2i data size",
    "index_disk_size": "2i size on disk",
    "index_total_scan_duration": "total time spent by 2i on scans",
    "index_items_count": "number of items in 2i",
    "query_avg_req_time": "Average processing time for N1QL",
    "query_avg_svc_time": "Average servicing time for N1QL",
    "query_avg_response_size": "Average response time for N1QL",
    "query_avg_result_count": "Average result count for N1QL",
    "query_active_requests": "N1QL avtive requests",
    "query_errors": "N1QL errors",
    "query_queued_requests": "N1QL queued requests",
    "query_request_time": "N1QL request times",
    "query_requests": "Query raw latency",
    "query_requests_1000ms": "Query latency above 1000ms",
    "query_requests_250ms": "Query latency above 250ms",
    "query_requests_5000ms": "Query latency above 5000ms",
    "query_requests_500ms": "Query latency above 500ms",
    "query_result_count": "N1QL result count",
    "query_result_size": "N1QL result size",
    "query_selects": "N1QL selects per second",
    "query_service_time": "N1QL service times",
    "query_warnings": "N1QL warnings",
    "cbft_num_bytes_used_disk": "FTS index size on disk in GB ",
    "cbft_doc_count": "FTS indexing rate",
    "cbft_num_bytes_used_ram": "FTS ram used by cbft process",
    "cbft_pct_cpu_gc": "FTS garbage collection CPU usage",
    "cbft_query_slow": "FTS slow query",
    "cbft_query_timeout": "FTS timeout query",
    "cbft_query_error": "FTS error query",
    "cbft_batch_merge_count":"FTS batch merge_count ",
    "cbft_total_gc" : "FTS garbage collector count",
    "cbft_num_bytes_live_data": "FTS live data size",
    "cbft_total_term_searchers": "FTS total term search ",
    "cbft_query_total" : "FTS total queries",
    "cbft_total_bytes_query_results": "FTS total query bytes",
    "cbft_writer_execute_batch_count": "FTS writer batch count",
    "cbft_latency_get": "FTS latency in ms",
    "elastic_latency_get": "ElasticSearch latency in ms",
    "cbft_total_bytes_indexed": "FTS total index size",
    "cbft_num_recs_to_persist": "FTS number of records in queue",
    "elastic_cache_hit": "Elasticsearch query cache hit",
    "elastic_cache_size": "Elasticsearch query cache size",
    "elastic_filter_cache_size": "Elasticsearch filter cache size",
    "elastic_active_search": "Elasticsearch active search",
    "elastic_query_total": "Elasticsearch total query",
}

HISTOGRAMS = (
    "latency_get", "latency_set", "latency_query", "latency_observe",
    "latency_persist_to", "latency_replicate_to",
    "xdcr_lag", "xdcr_persistence_time", "xdcr_diff",
    "replication_meta_latency_wt", "replication_docs_latency_wt",
    "avg_bg_wait_time", "avg_disk_commit_time", "avg_disk_update_time",
    "query_requests", "index_num_requests", "cbft_latency_get", "elastic_latency_get"

)

ZOOM_HISTOGRAMS = (
    "latency_get", "latency_set", "latency_query", "avg_bg_wait_time", "cbft_latency_get",
    "elastic_latency_get"
)

KDE = (
    "latency_query", "latency_get", "latency_set", "xdcr_lag", "cbft_latency_get",
    "elastic_latency_get"
)

SMOOTH_SUBPLOTS = (
    "latency_query", "latency_get", "latency_set", "cbft_latency_get",
    "elastic_latency_get"
)

NON_ZERO_VALUES = (
    "rebalance_progress",
    "bucket_compaction_progress",

    "ops",
    "cmd_get",
    "cmd_set",
    "delete_hits",
    "cas_hits",

    "couch_views_ops",
    "couch_views_data_size",
    "couch_views_actual_disk_size",
    "couch_views_fragmentation",
    "couch_docs_fragmentation",

    "hibernated_waked",

    "ep_tmp_oom_errors",
    "disk_write_queue",
    "ep_diskqueue_drain",
    "ep_cache_miss_rate",
    "ep_num_value_ejects",
    "ep_bg_fetched",
    "avg_bg_wait_time",
    "avg_disk_commit_time",
    "avg_disk_update_time",

    "xdc_ops",
    "ep_num_ops_get_meta",
    "ep_num_ops_set_meta",
    "ep_num_ops_del_meta",

    "replication_changes_left",
    "replication_size_rep_queue",
    "replication_rate_replication",
    "replication_bandwidth_usage",
    "replication_work_time",
    "replication_commit_time",
    "replication_active_vbreps",
    "replication_waiting_vbreps",
    "replication_num_checkpoints",
    "replication_num_failedckpts",
    "replication_meta_latency_wt",
    "replication_docs_latency_wt",

    "bucket_compaction_progress",

    "swap_used",

    "data_rbps",
    "data_wbps",
    "data_avgqusz",
    "data_util",
    "index_rbps",
    "index_wbps",
    "index_avgqusz",
    "index_util",

    "TIME_WAIT",
)

PALETTE = (
    "#51A351",
    "#f89406",
    "#7D1935",
    "#4A96AD",
    "#DE1B1B",
    "#E9E581",
    "#A2AB58",
    "#FFE658",
    "#118C4E",
    "#193D4F",
)
