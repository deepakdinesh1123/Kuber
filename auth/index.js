const Http = require("http");
const path = require("path");
require("dotenv").config();

const { issueToken, verifyToken } = require("./token");


const server = new Http.Server((req, res) => {
    console.log('Path parameters:', req.url);

    // Print headers
    console.log('Headers:', req.headers);


    // Print HTTP method
    console.log('Method:', req.method);

    // Parse URL parameters
    const urlParams = new URLSearchParams(req.url.slice(req.url.indexOf('?')));
    console.log('URL parameters:', Object.fromEntries(urlParams));

    const isAuthorized = true; // Replace with your own authorization logic

    // Set the appropriate response status based on authorization result
    const status = isAuthorized ? 200 : 403;

    // Send the response
    res.writeHead(status, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ authorized: isAuthorized }));
});

const port = process.env.PORT || 9002;
server.listen(port);
console.log(`starting HTTP server on: ${port}`);
