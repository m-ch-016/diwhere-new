<script>

</script>

<!-- <a href="/login">
    <div class="login">
        Login/Register    
    </div>
</a> -->


<style>
    a {
        text-decoration: none;
    }

    .login {
        color: #ffcb00;
        text-decoration: none;
        position: relative;
        z-index: 0;
        font-size: 1.5rem;
        padding: 0.5rem 2rem;
        transition: color 0.5s;
        border-radius: 1rem;
        overflow: hidden;
        box-shadow: 0 0 black;
    }

    .login::after {
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

    .login:hover {
        font-weight: 600;
        box-shadow: 0px 2px black;
        color: black;
    }

    .login:hover::after {
        height: 100%;
    }
</style>
