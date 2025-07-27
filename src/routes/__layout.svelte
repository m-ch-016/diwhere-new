<script>
  import Footer from "$lib/components/Footer.svelte";
  import Header from "$lib/components/Header.svelte";
  import Searchbox from "$lib/components/Searchbox.svelte";
  import { goto } from "$app/navigation";
  import LoginForm from "$lib/components/LoginForm.svelte";

  let products = [];

  const search = (term) => {
    console.log(term);
    goto("/results/" + term);
  };

  let loginvisible = false;

  const toggleLogin = () => {
    loginvisible = !loginvisible;
    console.log('login')
  };
</script>

<div class="container">
  <Header on:login={toggleLogin} />
<!-- 
  {#if loginvisible}
    <LoginForm />
  {/if} -->

  <main>
    <!-- <div class="searchbox"><Searchbox {search} /></div> -->
    <slot />
  </main>

  <Footer />
</div>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Raleway");

  .container {
    display: grid;
    grid-template-rows: auto 1fr auto;
    min-height: 100vh;
    font-family: Raleway, sans-serif;
  }

  a {
    text-decoration: none;
  }
</style>
