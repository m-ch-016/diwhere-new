<script>
  import ProductCard from "$lib/components/ProductCard.svelte";
  import { page } from "$app/stores";
  import { onMount } from "svelte";
  import Searchbox from "$lib/components/Searchbox.svelte";
  import { goto } from "$app/navigation";
  import LoadingWheel from "$lib/components/LoadingWheel.svelte";
  import ProductList from "$lib/components/ProductList.svelte";
  import PaintCard from "$lib/components/Paint-card.svelte";
  import { each } from "svelte/internal";

  let products = [];
  $: query = $page.url.searchParams.get("query");
  let order = 'Ascending'
  let sort = 'Price'
  let sources = [];

  $: {
    fetch(`http://127.0.0.1:5000/products?name=${query}&sort=${sort}&order=${order}`)
      .then((response) => response.json())
      .then((data) => {
        products = data.data;
      });
  }
  $: {
    fetch('http://127.0.0.1:5000/sources')
    .then((response) => response.json())
    .then((data) => {
        sources = data;
    });
  }

  const search = (query) => {
    goto(`/search?query=${query}`);
  };
</script>

<div class='container'>
  <div class="sort">
    <h3>Sort by:</h3>
    
    <button class="sortBtn" on:click={() => order = order==='Ascending'?'Descending':'Ascending'}>
      Order: {order}
    </button>

    <button class='sortBtn' on:click={() => sort = sort==='Price'?'Source':'Price'}>
      Sort: {sort}
    </button>
  </div>

  <div class="searchbox">
    <Searchbox {search} />
  </div>

  
  <div class="filter">
    {#each sources as source}
    <button>
      {source}
    </button>
    {/each}
  </div> 
</div>

{#if products.length === 0}
<div class="loading-wheel">
  <LoadingWheel />
</div>
{:else}
  <ProductList {products} />
{/if}

<style>
  .searchbox,
  .loading-wheel {
    align-items: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    align-items: center;
    justify-content: space-evenly;
    flex-direction: row;
    margin-top: 2rem;
  }

  .sort {
    display: flex;
    flex-direction: column;
  }

  button{
    text-decoration: inherit;
    font-family: Raleway;
    height: 2rem;
  }

  .sort h3 {
    margin-bottom: 1rem;
  }

  .filter {
    display: grid;
    grid-template-columns: auto auto auto;
  }

</style>
