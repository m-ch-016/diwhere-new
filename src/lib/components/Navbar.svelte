<script>
    import Navlink from "./Navlink.svelte";
    export let link;
</script>

<nav>
    <Navlink >
        <a href={link}>
            <slot />
        </a>
    </Navlink>
    
</nav>

<style>
    a{
        text-decoration: none;
        color: hsl(48,100%,50%);
    }

    a::after {
        content: "";
        height: 0;
        width: 100%;
        position: absolute;
        left: 0;
        bottom: 0;
        background-color: #ffcb00;
        z-index: -1;
        transition: 0.5s;
    }

    a:hover {
        font-weight: 600;
        box-shadow: 0px 2px black;
        color: black;
        text-decoration: none;
    }

    a:hover::after {
        text-decoration: none;
        height: 100%;
    }

    slot {
        color: black;
    }
    nav {
        display: flex;
        gap: 1rem;
        /* justify-content: space-evenly; */
    }
    Navlink {
        border-left: 1px solid black;
        color: white;
        border-left: 1px solid black;
    }

    Navlink:first-child {

    }
    
    Navlink:last-child {
        border-right: 1px solid black;
        /* margin-left: rem; */
    }
    
</style>
