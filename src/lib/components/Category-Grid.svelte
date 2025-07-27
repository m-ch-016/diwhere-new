<script>
  import BathroomCard from "./Bathroom-card.svelte";
  import BlankCard from "./Blank-card.svelte";
  import BuildingCard from "./Building-card.svelte";
  import ClearanceCard from "./Clearance-card.svelte";
  import FurnitureCard from "./Furniture-card.svelte";
  import HeatingCard from "./Heating-card.svelte";
  import KitchenCard from "./Kitchen-card.svelte";
  import OutdoorCard from "./Outdoor-card.svelte";
  import PaintCard from "./Paint-card.svelte";
  import PlumbingCard from "./Plumbing-card.svelte";
  import TilingCard from "./Tiling-card.svelte";
  import TimberCard from "./Timber-card.svelte";
  import ToolsCard from "./Tools-card.svelte";
  import WiringCard from "./Wiring-card.svelte";
</script>

<div class="category-grid">
  <BathroomCard />
  <BuildingCard />
  <WiringCard />
  <FurnitureCard />
  <HeatingCard />
  <KitchenCard />
  <OutdoorCard />
  <PaintCard />
  <PlumbingCard />
  <TilingCard />
  <TimberCard />
  <ToolsCard />
</div>

<style>
  .category-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
  }
</style>
