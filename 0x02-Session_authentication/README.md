# alx-backend-user-data
## Session Based Authentication

Session authentication using cookies:

1. User logs in:
    - User submits credentials (username/password)
    - Server verifies credentials

2. Server creates session:
    - Generates a unique session ID
    - Stores session data server-side (e.g. in memory, database)

3. Server sends a cookie:
    - Sets a cookie containing the session ID
    - Typically includes attributes like HttpOnly, Secure, SameSite

4. Subsequent requests:
    - The browser automatically sends the cookie
    - The server retrieves session data using the session ID
    - Authenticates the user based on session data

5. Logout:
    - The server invalidates the session
    - Instructs the browser to delete the cookie

This mechanism allows stateless HTTP to maintain user authentication across requests without repeatedly sending credentials.

## Token storage: A session ID is stored in the cookie, while actual session data is stored server-side.
## Stateful: The server maintains session information.
## Cookie content: Contains only a session identifier.
## Scalability: Can be less scalable due to server-side storage requirements.
## Security: Generally considered more secure as sensitive data is kept server-side

#  Cookies
## is a small piece of data a server sends to a user's web browser.
## The browser stores this data in a small file called a cookie.
## When the user makes another request to the server, the browser sends back the cookie.
## The server can then use the cookie to identify the user and tailor its response.
## Cookies can be used for authentication, tracking, and personalization.
## Cookies can be set to expire after a certain period of time or when the user closes their browser
## Cookies can be set to be secure, which means they can only be transmitted over a secure connection
## Cookies can be set to be http only, which means they can only be accessed by the server
## Cookies can be set to be same site, which means they can only be accessed by the same site that set them
