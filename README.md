Deploy on remote server - 

Using fastmcp.cloud which connects to github repo and generates an MCP server address to be used (https://wide-aqua-wolverine.fastmcp.app/mcp)

Connecting Claude to the remote server is not possible directly in free plan using connectors - 

To solve this fastmcp provides concept of proxy

Client connects to Proxy Server which in turn connects to MCP Server (remote server)
Remote server responds to Proxy Server which then responds to the Client

client <----> proxy server <----> remote mcp server


Install uv - pip3 install uv

Initiate a project - uv init .

Install fastmcp - uv add fastmcp

Test the server - uv run fastmcp dev main.py -> opens MCP Inspector for testing

Run the server - uv run fastmcp run main.py

Add local server to Claude Desktop - uv run fastmcp install claude-desktop main.py

Add proxy server to Claude Desktop - uv run fastmcp install claude-desktop proxy.py