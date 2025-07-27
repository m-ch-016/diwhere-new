<script context="module">
    export function load({ error, status }) {
        return {
            props: {
                error,
                status,
            },
        };
    }
</script>

<script lang="ts">
    import { onMount } from "svelte";

    export let error;
    export let status;

    onMount(() => {
        const container:HTMLDivElement = document.querySelector("#container");
        window.addEventListener("mousemove", (e) => {
            const x = -e.clientX / 5
            const y = -e.clientY / 5;
            container.style.backgroundPositionX = x + "px";
            container.style.backgroundPositionY = y + "px";
        });
    });
</script>

<body>
    <div id="container">
        <div class="content">
            <h2>{status}</h2>
            <h4>
                Hmmmm... Seems like this page doesn't exist! Have a look to see
                if you've searched for the wrong thing!
            </h4>
            <a href="/">Back To Home</a>
        </div>

        <p>Error {status}: {error.message}</p>
    </div>
</body>

<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: "Raleway", sans-serif;
    }

    /* body {
        background: linear-gradient(45deg, #8500ff, #5acaff); */
        /* height: 100vh; */
    

    #container {
        height: 100%;
        width: 100%;
        top: 10%;
        left: 10%;
        bottom: 10%;
        right: 10%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: url("p404.png") #151729;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
        padding-bottom: 5em;
        padding-top: 5em;
    }

    #container .content {
        max-width: 600px;
        text-align: center;
    }

    #container .content h2 {
        font-size: 14vw;
        color: gainsboro;
        line-height: 1em;
        margin-bottom: 2vw;
    }

    #container .content h4 {
        position: relative;
        font-size: 1.5em;
        margin-bottom: 20px;
        color: gainsboro;
        font-weight: 300;
        padding: 10px 20px;
        display: inline-block;
    }

    #container .content p {
        color: gainsboro;
        font-size: 1.2em;
    }

    #container .content a {
        position: relative;
        display: inline-block;
        padding: 10px 25px;
        background-color: #ff0562;
        color: gainsboro;
        text-decoration: none;
        margin-top: 25px;
        border-radius: 25px;
        border-bottom: 4px solid #d00d56;
        margin-bottom: 2rem;
    }

    #container p {
        color: gainsboro;
    }
</style>
