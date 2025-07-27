<div class="header-card">
    <div class="header-title">
        Image
    </div>
    
    <div class="header-title">
        Description
    </div>

    <div class="header-title">
        Price
    </div>
    
    <div class="header-title">
        Company
    </div>
    
    <div class="header-title">
        Website Link
    </div>
    
</div>

<style>
    .header-card {
        display: grid;
        grid-template-columns: repeat(5 , 1fr);
        background-color: aliceblue;
        border-radius: 1rem;
        border: 1px solid gainsboro;
        margin-top: 2rem;
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    .header-title {
        border-right: 0.1rem solid gainsboro;
    }

    .header-title:last-child {
        border-right: 0px;
    }

    .header-title {
        display: flex;
        font-size: 2.5rem;
        align-items: center;
        justify-content: center;
    }
</style>