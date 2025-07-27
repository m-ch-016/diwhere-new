<script>
import Bathstore from "./Bathstore.svelte";

    import BnqCard from "./BnqCard.svelte";
    import FrontlineCard from "./FrontlineCard.svelte";
    import HomebaseCard from "./HomebaseCard.svelte";
    import Homebase from "./HomebaseCard.svelte";
    import JewsonCard from "./JewsonCard.svelte";
    import RexelCard from "./RexelCard.svelte";
    import ScrewfixCard from "./ScrewfixCard.svelte";
    import SelcoCard from "./SelcoCard.svelte";
    import ToolstationCard from "./ToolstationCard.svelte";
    import VictoriaPlumCard from "./VictoriaPlumCard.svelte";
    import WickesCard from "./WickesCard.svelte";
    import WoodiesCard from "./WoodiesCard.svelte";
</script>

<div class="brands-grid">
    <BnqCard />
    <FrontlineCard />
    <HomebaseCard />
    <JewsonCard />
    <RexelCard />
    <ScrewfixCard />
    <SelcoCard />
    <ToolstationCard />
    <VictoriaPlumCard />
</div>
<div class="bottom-brands-grid">
    <WickesCard />
    <WoodiesCard />
</div>

<!-- <div class="bottom-brands-grid">
</div> -->

<style>
  .brands-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
  }

  .bottom-brands-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      padding-left: 12%;
  }
</style>
