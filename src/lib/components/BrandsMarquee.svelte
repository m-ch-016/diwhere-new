<div class="marquee">
    <div class="inner">
        <slot />
    </div>
</div>

<style>

    * {
        outline: 1px solid red;
    }
    .marquee {
        position: relative;
        overflow: hidden;
        width: calc(100% - 16rem);
    }
    
    .inner {
        display: flex;
        gap: 2rem;
        align-items: center;
        position: relative;
        animation: marquee 20s linear infinite;
    }

    @keyframes marquee {
        0% {
            transform: translateX(0%);
        }

        100% {
            transform: translateX(-100%);
        }

        
        
    }

</style>