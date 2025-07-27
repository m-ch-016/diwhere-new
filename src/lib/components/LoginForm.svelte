<script>
    let container;

    let showregister = false;

    const toggleregister = () => {
        showregister = !showregister;
    };
</script>

<section>
    <div class="container">
        {#if !showregister}
            <div class="user loginbx">
                <div class="imgbx">
                    <img class="lockimg" src="../static/lockimg.png" alt="" />
                </div>
                <div class="formbx">
                    <h2>Login</h2>
                    <input type="text" placeholder="Username..." />
                    <input type="password" placeholder="Password..." />
                    <input type="submit" value="Login" />
                    <a href='' class="signup">Don't have an account? <span class="click" on:click={toggleregister}> <span>Click</span> <span>here</span>  to sign up!</span></a>
                </div>
            </div>
        {:else}
            <div class="user signupbx">
                <div class="imgbx">
                    <img class="keyimg" src="../static/keysimg.jpg" alt="" />
                </div>
                <div class="formbx">
                    <h2>Register</h2>
                    <input type="text" placeholder="Username..." /><input
                        type="text"
                        placeholder="Email address..."
                    />
                    <input type="tel" placeholder="Phone number..." /><input
                        type="password"
                        placeholder="Create Password..."
                    /><input
                        type="password"
                        placeholder="Confirm Password..."
                    /><input type="submit" value="Signup" />
                    <a href='' class="signup">
                        Already have an account? <span class="click" on:click={toggleregister}
                            ><span>Click</span> <span>here</span>  <span>to</span>  <span>login!</span> </span>
                    </a>
                </div>
            </div>
            {/if}
    </div>
</section>

<!-- 
{#if !showregister}
    <div class="form">
        <h2>Login</h2>
        <input type="text" placeholder="Username..." />
        <input type="password" placeholder="Password..." />
        <input type="submit" value="Login" />
        <p class="signup">
            Don't have an account? <span on:click={toggleregister}>
                Click here to sign up!</span
                >
        </p>
    </div>
    {:else}<div class="form">
        <h2>Register</h2>
        <input type="text" placeholder="Username..." /><input
        type="text"
        placeholder="Email address..."
        />
        <input type="tel" placeholder="Phone number..." /><input
            type="password"
            placeholder="Create Password..."
        /><input type="password" placeholder="Confirm Password..." /><input
            type="submit"
            value="Signup"
        />
        <p class="signup">
            Already have an account? <span on:click={toggleregister}
                >Click here to login!</span
            >
        </p>
    </div>{/if} -->
<style>
    section {
        position: absolute;
        right: 0;
        bottom: 0;
        top: 0;
        left: 0;
        background: hsla(0, 0%, 0%, 0.2);
        display: grid;
        place-content: center;
    }

    .container {
        background: white;
    }

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    section {
        position: relative;
        min-height: 100vh;
        background-color: #b6bbc3;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
        transition: 0.5s;
    }

    .lockimg {
        width: 100%;
        height: 100%;
    }

    section .container {
        position: relative;
        width: 800px;
        height: 500px;
        background: white;
        box-shadow: 0px 15px 50px rgba(0, 0, 0, 0.1);
        overflow: hidden;
        border-radius: 2rem;
    }

    section .container .user {
        position: absolute;
        top: 0;
        right: 0;
        width: 100%;
        height: 100%;
        display: flex;
    }
    section .container .user .imgbx {
        position: relative;
        width: 50%;
        height: 100%;
        transition: 0.5s;
    }

    section .container .user .imgbx img {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    section .container .user .formbx {
        position: relative;
        width: 50%;
        height: 100%;
        background-color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        padding: 40px;
        transition: 0.5s;
    }

    section .container .user .formbx h2 {
        font-size: 18px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-align: center;
        width: 100%;
        margin-bottom: 10px;
        color: #555;
    }

    section .container .user .formbx input {
        width: 100%;
        font-family: Raleway, sans-serif;
        padding: 10px;
        background-color: #f5f5f5;
        background-color: rgb(193, 201, 213);
        border-radius: 1rem;
        color: #333;
        border: none;
        outline: none;
        box-shadow: none;
        font-size: 14px;
        margin: 8px 0px;
        letter-spacing: 1px;
        font-weight: 500;
    }

    section .container .user .formbx input[type="submit"] {
        max-width: 100px;
        background-color: hsl(185, 96%, 19%);
        color: white;
        cursor: pointer;
        font-size: 14px;
        font-weight: 500;
        letter-spacing: 1px;
        transition: 0.5s;
    }

    section .container .user.signupbx .formbx input[type="submit"] {
        background: #e73e49;
    }

    section .container .user .formbx .signup {
        position: relative;
        margin-top: 20px;
        font-size: 12px;
        letter-spacing: 1px;
        color: #555;
        text-transform: uppercase;
        font-weight: 300;
    }

    section .container .user .formbx .signup a {
        font-weight: 600;
        text-decoration: none;
        color: #577eff;
    }

    section .container .signupbx {
        pointer-events: initial;
    }

    section .container.active .signupbx .formbx {
        top: 100%;
        transition: 0.5s;
        /* display: block; */
    }
    
    section .container.active .signupbx .formbx {
        top: 0;
    }

    section .container.active .signupbx .imgbx {
        top: -100%;

    }

    section .container .signupbx .imgbx {
        top: 0;
        transition: 0.5s;
    }

    section .container .loginbx .formbx {
        top: 0;
    }

    section .container.active .loginbx .formbx {
        top: -100%;
        transition: 0.5s;
    }

    section .container .loginbx .imgbx {
        top: 0;
        transition: 0.5s;
    }
    
    section .container.active .loginbx .imgbx {
        top: -100%; 
        transition: 0.5s;
    }


    section .container .loginbx .formbx {
        top: 0;
    }

    section .container.active .loginbx .formbx {
        top: 100%;
    }

    /* section .container */

    .click  span:nth-child(2) {
        font-weight: 750;
    }
</style>
