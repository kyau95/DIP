<script lang="ts">
  import Icon from "./Icon.svelte";
  const props = $props();
  const data = $derived(props.data);
  const currencySymbol = $derived(props.currency);
</script>

<!-- TODO: Take in an image URL, user can hover over the product name column and see the item-->

{#if props.isHeader}
  <tr>
    <th>Product Name</th>
    <th>Tracker Price</th>
  </tr>
{:else}
  <tr>
    <td>
      {data["productName"]}
      <Icon url={data["url"]} />
    </td>
    <td>{currencySymbol}{data["price"]}</td>
  </tr>
{/if}

<style>
  th {
    background-color: #f2f2f2;
    color: #333;
    font-weight: bold;
    padding: 12px;
    text-align: center;
    border-bottom: 2px solid #333333;
  }

  th:first-child {
    border-top-left-radius: var(--default-border-radius);
  }

  th:last-child {
    border-top-right-radius: var(--default-border-radius);
  }

  td {
    padding: 12px;
    border-bottom: 1px solid #cccccc;
    text-overflow: ellipsis;
    overflow: hidden;
  }

  /* Column dividers (adds border to all but the last column) */
  th:not(:last-child),
  td:not(:last-child) {
    border-right: 1px solid #cccccc;
  }

  /* Removes the bottom border from the very last row */
  tr:last-child td {
    border-bottom: none;
  }
</style>
