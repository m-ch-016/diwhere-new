<script>
    export let product;
    import ProductLogo from "./ProductLogo.svelte";
</script>

<div class="product-card">
    <img src={product.image} alt={product.name}>
    <h2>{product.name}</h2>
    <h3 class = 'price'>£{product.price}</h3>
    <div class="product-link">
        <a target="_blank" href={product.link}>Go to&nbsp;<ProductLogo source={product.source}/></a>
    </div>
</div>


<style>
    * {
       /* outline: 1px solid red;  */
    }

    .product-card  {
        /* outline: 1px solid red; */
        padding: 2rem;
        border-radius: 2rem;
        box-shadow: 1px 1px 3px black;
        transition: box-shadow 0.5s, transform 0.5s;
        display: flex;
        flex-direction: column;
        align-items: stretch;
        gap: 1rem;
    }

    .product-card:hover {
        /* box-shadow: 0 0.5rem 1rem 0 black; */
        /* transform: scale(1.01); */
    }

    img {
        width: 100%;
        aspect-ratio: 1;
        align-items: center;
    }

    .product-link {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        align-self: flex-end;
    }

    .product-link a {
        padding: 1rem;
        border-radius: 1rem;
        
        font: inherit;
        background-color: hsl(185, 96%, 19%);
        color: hsl(48, 100%, 50%);
        font-weight: 650;
        position: relative;
        overflow: hidden;
        transition: 0.5s;
        z-index: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .product-link a::before {
        position: absolute;
        left: 0;
        bottom: 0;
        height: 0%;
        width: 100%;
        content: "";
        background-color: hsl(48, 100%, 50%);
        transition: height 0.5s;
        z-index: -1;
    }

    .product-link a:hover::before {
        height: 100%;
    }

    .product-link a:hover {
        color: black;
    }

    ProductLogo {
        
    }

    h3 {
        flex: 1 ;
    }

    .price {
        color: #D01345;
        font-size: 2rem;
    }
</style>