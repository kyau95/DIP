<script lang="ts">
  import ProductRow from "./ProductRow.svelte";
  import { onMount } from "svelte";
  import { getProducts } from "../api";
  
  interface Product {
    id: number;
    productName: string;
    price: string;
    url: string;
    currency: string;
  };

  // let data = [
  //   {
  //     id: 1,
  //     productName: "Audio-Technica ATH-WP900 On-Ear Headphones (Flamed Maple)",
  //     price: "$699.00",
  //     url: "https://www.target.com/p/audio-technica-ath-wp900-on-ear-headphones-flamed-maple/-/A-1001263584#lnk=sametab"
  //   },
  //   {
  //     id: 2,
  //     productName: "MSI Ventus GeForce RTX 5060 Ti 8GB GDDR7 PCI Express® Gen 5 x16 (uses x8) ATX Graphics Card RTX 5060 Ti 8G VENTUS 3X OC",
  //     price: "$419.99",
  //     url: "https://www.newegg.com/msi-rtx-5060-ti-8g-ventus-3x-oc-geforce-rtx-5060-ti-8gb-graphics-card-triple-fans/p/N82E16814982007"
  //   },
  //   {
  //     id: 3,
  //     productName: "The Court Sneaker",
  //     price: "$89.00",
  //     url: "https://www.everlane.com/products/womens-court-sneaker-white-grass-green?variant=42973788078166"
  //   },
  //   {
  //     id: 4,
  //     productName: "GameSir T7 Wired Controller for Xbox Series X|S, Xbox One & Windows 10/11, Plug and Play Gaming Gamepad with Hall Effect Joysticks/Hall Trigger, 3.5 mm Audio Jack - White",
  //     price: "$28.49",
  //     url: "https://www.walmart.com/ip/GameSir-T7-Wired-Controller-Xbox-Series-X-S-Xbox-One-Windows-10-11-Plug-Play-Gaming-Gamepad-Hall-Effect-Joysticks-Hall-Trigger-White-Version/9374812633?classType=VARIANT&adsRedirect=true"
  //   }
  // ];

  let products: Product[] = $state([]);
  onMount(async () => {
    products = await getProducts();
  });
</script>

<div>
  <div class="button-row">
    <!-- TODO: Add a search feature -->
    <!-- <textarea placeholder="Search Item..."></textarea> -->
    <button><b>Add New Item</b></button>
  </div>

  <table>
    <tbody>
      <ProductRow isHeader={true} />
      {#each products as item (item.id)}
        <ProductRow isHeader={false} data={item} />
      {/each}
    </tbody>
  </table>
</div>

<style>
  .button-row {
    width: 100%;
    height: 56px;
  }
  
  button {
    float: right;
    padding: 8px 32px;
    border-radius: var(--default-border-radius);
    cursor: pointer;
    
    font-size: 1em;
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  }

  button:hover {
    background-color: #c0c0c025;
  }

  button:active {
    transform: scale(0.99);
  }

  table {
    border: 2px solid;
    border-radius: var(--default-border-radius);
    border-collapse: separate;
    border-spacing: 0;

    text-align: center;
    font-size: 1em;
    min-width: 800px;
    max-width: 1600px;
  }
</style>
