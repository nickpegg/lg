# Nick's Looking Glass

This is a simple looking glass tool, supports pinging and MTRing arbitrary addresses. Doesn't support BGP tables like a lot of looking glass tools do since I don't personally own a router that speaks it with the internet.


## Caveats

I recommend running this as a non-privileged user stuck inside of rbash. I tried to keep people from injecting commands, but you can never be too cautious.

I also don't do any rate-limiting since whatever front-end webserver you choose (nginx, apache, etc.) is better suited to that task.
