<script>
  import Social from "./Social.svelte";

</script>
<div class="wrapper-main">
    <div class="socials">
        <div class="social social-twitter">
            <Social link='/' icon='fa fa-twitter'></Social>
        </div>
        <div class="social social-facebook">
            <Social link='/' icon='fa fa-facebook'></Social>
        </div>
        <div class="social social-tiktok">
            <Social link='/' icon='fa fa-tiktok'></Social>
        </div>
        <div class="social social-instagram">
            <Social link='/' icon='fa fa-instagram'></Social>
        </div>
    </div>

    <div class="contact-us">
        <h3>Problem?</h3>
        <h5>Contact us at: <a href='mailto:help@diwhere.com'>help@diwhere.com</a></h5>
    </div>
</div>


<style>
    .wrapper-main {
        height: fit-content;
        background-color: hsl(165, 100%, 14%);
        display: flex;
        flex-direction: column;
    }

    .socials {
        display: flex;
        flex-direction: row;
        border-bottom: 1px solid rgba(220, 220, 220, 0.353);
        padding-bottom: 1rem;
        flex-wrap: wrap;
        margin-top: 3rem;
        margin-left: 37%;
        width: fit-content;
        align-items: center;
        justify-content: center;

    }

    .social {
        margin-left: 1.5rem;
        margin-right: 1.5rem;
    }

    .contact-us {
        padding-top: 2rem;
        justify-content: center;
        align-items: center;
        display: flex;
        flex-direction: column;
        color: #ffcb00;
    }

    .contact-us a {
        color: rgb(220, 220, 220);
    }
</style>