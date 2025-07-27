<script>
  export let search;

  let term="";

  const onkeyup = (event) => {
    if (event.code === "Enter") {
      search(term)
    }
  }
  
  const onclick = (event) => {
    search(term)
  }
  
</script>

<div class="searchbox">
  <input
    type="text"
    placeholder="Search, Click, Collect..."
    on:keyup={onkeyup}
    bind:value={term}
  />
  <i on:click={onclick} class="fas fa-search" />
</div>

<style>
  .searchbox {
    position: relative;
    width: 95px;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 1rem;
    overflow: hidden;
    transition: 0.5s;
    box-shadow: -5px -5px 10px 0px #ebecff, 5px 5px 10px 0px #a4a5b3;
    margin-bottom: 2rem;
    margin-top: 2rem;
  }

  .searchbox:hover {
    width: 400px;
    transition: 0.6s ease-in-out;
  }

  .searchbox input {
    font-family: Raleway, sans-serif;
    font-size: 1.25rem;
    font-weight: 750;
    position: relative;
    width: 100%;
    height: 100%;
    border: none;
    padding: 0px 25px;
    outline: none;
    color: #555;
    background-color: #cfd1e1;
    padding-right: 50px;
    box-shadow: inset -5px -5px 20px 0px #ebecff, inset 5px 5px 20px 0px #a4a5b3;
  }

  .searchbox input::placeholder,
  .searchbox input {
    color: transparent;
  }

  .searchbox:hover input::placeholder,
  .searchbox:hover input {
    color: #555;
  }

  .searchbox:has(+text) {
    width: 400px;
  }

  .fa-search {
    z-index: 1000;
    position: absolute;
    color: #004735;
    font-size: 1.5em;
    right: 20px;
    cursor: pointer;
  }
</style>
