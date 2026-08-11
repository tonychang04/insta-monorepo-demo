require("http").createServer((_, r) => { r.writeHead(200, {"Content-Type":"text/html"}); r.end("<h1>web service — Node, no Dockerfile, via nixpacks</h1>"); }).listen(process.env.PORT || 3000);
