<script>
    import ProductCard from '$lib/components/ProductCard.svelte'
    import ProductHeader from './ProductHeader.svelte';
    export let products;
</script>

<div class="container">
    <!-- <div class="product-header">
        <ProductHeader />
    </div> -->
    <div class="products-display">
        {#each products as product}
            <ProductCard {product} />
        {/each}
    </div>
</div>


<style>
    
    .container {
        display: flex;
        flex-direction: column;
    }

    .product-header {
        padding-left: 2rem;
        padding-right: 2rem;
        margin-bottom: 0;
    }

    .products-display {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 2rem;
        padding: 2rem;
    }

</style>