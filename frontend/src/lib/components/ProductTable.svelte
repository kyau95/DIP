<script lang="ts">
  import ProductRow from "./ProductRow.svelte";
  import { onMount } from "svelte";
  import { getProducts } from "../api";
    import AddItemModal from "./AddItemModal.svelte";

  interface Product {
    id: string;
    productName: string;
    price: string;
    url: string;
    currency: string;
  }
  let products: Product[] = $state([]);
  let showModal = $state(false);

  onMount(async () => {
    products = await getProducts();
  });
</script>

<AddItemModal bind:showModal />

<div>
  <div class="button-row">
    <!-- TODO: Add a search feature -->
    <!-- <input placeholder="Search Item..."></input> -->
    <button onclick={() => showModal = true}><b>Add New Item</b></button>
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
    height: 72px;
  }

  button {
    float: right;
    padding: 20px 42px;
    border-radius: var(--default-border-radius);
    cursor: pointer;
    border: none;
    font-weight: bold;
    font-size: 1em;
    font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
      "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
    background-color: #3b82f6;
    color: white;
    box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.2);
    transition: background-color 0.2s ease, transform 0.1s ease, box-shadow 0.2s ease;
  }

  button:hover {
    background-color: #2563eb;
    box-shadow: 0 6px 10px -1px rgba(59, 130, 246, 0.3);
  }

  button:active {
    transform: scale(0.96);
  }

  table {
    border-collapse: separate;
    border-spacing: 0;
    border: 1px solid #e5e7eb;
    border-radius: var(--default-border-radius);
    overflow: hidden;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.02);

    text-align: left;
    font-size: 0.95em;
    min-width: 800px;
    max-width: 1600px;
    background-color: white;
  }
</style>
