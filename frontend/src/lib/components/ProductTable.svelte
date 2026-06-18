<script lang="ts">
  import ProductRow from "./ProductRow.svelte";
  import { onMount } from "svelte";
  import { getProducts } from "../api";

  interface Product {
    id: string;
    productName: string;
    price: string;
    url: string;
    currency: string;
  }
  let products: Product[] = $state([]);
  let { addItemEvent } = $props();

  onMount(async () => {
    products = await getProducts();
  });
</script>

<div>
  <div class="button-row">
    <!-- TODO: Add a search feature -->
    <!-- <textarea placeholder="Search Item..."></textarea> -->
    <button onclick={addItemEvent}><b>Add New Item</b></button>
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
    font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
      "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
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
