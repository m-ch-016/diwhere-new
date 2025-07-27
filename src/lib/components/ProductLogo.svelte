<script>
    export let source;
</script>

{#if source === "bnq"}
            <img class="bnq" src="/static/bnqlogo.png" alt="" />
        {/if}

        {#if source === "bathstore"}
            <img class="bathstore" src="/static/bathstorelogo.png" alt="" />
        {/if}

        {#if source === "frontline"}
            <img class="frontline" src="/static/frontlinelogo.png" alt="" />
        {/if}

        {#if source === "homebase"}
            <img class="homebase" src="/static/homebaselogo.png" alt="" />
        {/if}

        {#if source === "jewson"}
            <img class="jewson" src="/static/jewsonlogo.png" alt="" />
        {/if}

        {#if source === "rexel"}
            <img class="rexel" src="/static/rexellogo.png" alt="" />
        {/if}

        {#if source === "screwfix"}
            <img class="screwfix" src="/static/screwfixlogo.png" alt="" />
        {/if}

        {#if source === "selco"}
            <img class="selco" src="/static/selcologo.png" alt="" />
        {/if}

        {#if source === "toolstation"}
            <img class="toolstation" src="/static/toolstationlogo.png" alt="" />
        {/if}

        {#if source === "victoria plum"}
            <img class="vicplum" src="/static/victoriaplumlogo.png" alt="" />
        {/if}

        {#if source === "wickes"}
            <img class="wickes" src="/static/wickeslogo.png" alt="" />
        {/if}

        {#if source === "woodies"}
            <img class="woodies" src="/static/woodieslogo.png" alt="" />
        {/if}

<style>
    img {
        height: 2rem;
    }

    .vicplum {
        height: 3rem;
        width: 4rem;
    }
</style>