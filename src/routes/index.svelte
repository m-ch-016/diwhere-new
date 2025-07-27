<script>
  import CategoryGrid from "$lib/components/Category-Grid.svelte";
  import Searchbox from "$lib/components/Searchbox.svelte";

  import { goto } from "$app/navigation";
  import BrandsGrid from "$lib/components/BrandsGrid.svelte";
  import LoginForm from "$lib/components/LoginForm.svelte";

  import { user } from "$lib/components/stores.js"
  import { get } from "svelte/store";
  import Footer from "$lib/components/Footer.svelte";

  
  let products = [];

  const search = (query) => {
    console.log(query);
    goto(`/search?query=${query}`);

  };
</script>

<svelte:head>
  <script
    src="https://kit.fontawesome.com/d397854d5c.js"
    crossorigin="anonymous"></script>
</svelte:head>

<div class="wrapper-main">
  
  <h2>Search for products anywhere!</h2>

  <div class="searchbox">
    <Searchbox {search} />
  </div>

  <div class="category-grid">
    <CategoryGrid />
  </div>

</div>

<style>
  .searchbox {
    align-items: center;
    display: flex;
    justify-content: center;
  }
  .wrapper-main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding-top: 2rem;
  }


</style>
