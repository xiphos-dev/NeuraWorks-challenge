-- example HTTP POST script which demonstrates setting the
-- HTTP method, body, and adding a header

wrk.method = "POST"
wrk.body   = {DIA:1,MES:1,TIPOVUELO:"I",OPERA:"American Airlines",SIGLADES:"Miami"}
wrk.headers["Content-Type"] = "application/json"
