<script>
    export let product;

    let prodsource = product.source;
    let rating = product.rating;
    let prodprice = product.price;

    let clicks = product.clicks;

    const updateclicks = () => {
        fetch("http://127.0.0.1:5000/update/" + product[0])
            .then((response) => response.json())
            .then((data) => {
                clicks = data.clicks;
            });
    }
    // products.append((p.id, p.name, p.price, p.weblink, p.image, p.source, p.clicks))
</script>

<div class="product-card">
    <div class="product-img">
        <img src={product.image} alt="" />
    </div>

    <div class="product-title">
        {product.name}
    </div>

    <div class="product-price">
        {#if prodprice !== null}

            {#if prodsource === "bnq"}
                <div style="font-size:0.65em">
                    £{product.price}
                </div>
            {/if}

            {#if prodsource === "bathstore"}
                <div style="font-size:0.65em">
                    £{product.price}
                </div>
            {/if}

            {#if prodsource === "frontline"}
                <div style="font-size:0.65em">
                    £{product.price}
                </div>
            {/if}

            {#if prodsource === "homebase"}
                <div style="font-size:0.65em">
                    £{product.price}
                </div>
            {/if}

            {#if prodsource === "jewson"}
                <div style="font-size:0.65em">
                    £{product.price}
                </div>
            {/if}

            {#if prodsource === "rexel"}
                <div style="font-size:0.65em">
                    £{product.price}
                </div>
            {/if}

            {#if prodsource === "screwfix"}
                <div style="font-size:0.65em">
                    £{product.price}
                </div>
            {/if}

            {#if prodsource === "selco"}
                <div style="font-size:0.65em">
                    £{product.price}
                </div>
            {/if}

            {#if prodsource === "toolstation"}
                <div style="font-size:0.65em">
                    £{product.price}
                </div>
            {/if}

            {#if prodsource === "victoriaplum"}
                <div style="font-size:0.65em">
                    £{product.price}
                </div>
            {/if}

            {#if prodsource === "wickes"}
                <div style="font-size:0.65em">
                    £{product.price}
                </div>
            {/if}

            {#if prodsource === "woodies"}
                <div style="font-size:0.65em">
                    {product.price}
                </div>
            {/if}

            {:else}
            <div style='font-size:0.45em'>
                NO PRICE GIVEN
            </div>
        {/if}
    </div>

    <div class="product-src">
        {#if prodsource === "bnq"}
            <img class="bnq" src="/static/bnqlogo.png" alt="" />
        {/if}

        {#if prodsource === "bathstore"}
            <img class="bathstore" src="/static/bathstorelogo.png" alt="" />
        {/if}

        {#if prodsource === "frontline"}
            <img class="frontline" src="/static/frontlinelogo.png" alt="" />
        {/if}

        {#if prodsource === "homebase"}
            <img class="homebase" src="/static/homebaselogo.png" alt="" />
        {/if}

        {#if prodsource === "jewson"}
            <img class="jewson" src="/static/jewsonlogo.png" alt="" />
        {/if}

        {#if prodsource === "rexel"}
            <img class="rexel" src="/static/rexellogo.png" alt="" />
        {/if}

        {#if prodsource === "screwfix"}
            <img class="screwfix" src="/static/screwfixlogo.png" alt="" />
        {/if}

        {#if prodsource === "selco"}
            <img class="selco" src="/static/selcologo.png" alt="" />
        {/if}

        {#if prodsource === "toolstation"}
            <img class="toolstation" src="/static/toolstationlogo.png" alt="" />
        {/if}

        {#if prodsource === "victoriaplum"}
            <img class="vicplum" src="/static/victoriaplumlogo.png" alt="" />
        {/if}

        {#if prodsource === "wickes"}
            <img class="wickes" src="/static/wickeslogo.png" alt="" />
        {/if}

        {#if prodsource === "woodies"}
            <img class="woodies" src="/static/woodieslogo.png" alt="" />
        {/if}
    </div>

    <!-- <a href={product[2]}> -->
    <div class="product-link">
        <a target="_blank" href={product.link + '?referred=yes'}>Take me to the website</a>
    </div>

    <!-- </a> -->
    <!-- get bnq image in bottom corner -->
</div>

<style>
    * {
        /* outline: 1px solid green; */
    }
    .product-card {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        border: 0.1rem solid black;
        border-radius: 1rem;
        overflow: hidden;
    }

    .bathstore {
        width: 450px;
        height: 100px;
    }

    .product-img,
    .product-title,
    .product-price,
    .product-src,
    .product-link{
        border-right: 0.1rem solid gainsboro;
        display: flex;
        padding: 2rem;
        justify-content: center;
        align-items: center;
        font-size: 1.5rem;
    }

    .product-title {
        font-weight: 650;
        text-transform: capitalize;
    }

    .product-price {
        font-size: 3.75rem;
        font-weight: 650;
        color: hsl(185, 96%, 19%)
    }

    .product-link {
        border-right: none;
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

    .product-src img.bnq {
        width: 65%;
        height: 85%;
    }
</style>
