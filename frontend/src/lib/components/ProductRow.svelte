<script lang="ts">
  import Icon from "./Icon.svelte";
  const props = $props();
  const data = $derived(props.data);
</script>

{#if props.isHeader}
  <tr>
    <th>Product Name</th>
    <th>Tracker Price</th>
  </tr>
{:else}
  <tr>
    <td>{data["productName"]} <Icon url={data["url"]} /></td>
    <td>{data["price"]}</td>
  </tr>
{/if}

<style>
  /* th, td {
    border: 1px solid;
    text-align: center;
    padding: 12px 0;
  } */
  /* Header styles */
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

  /* Cell styles */
  td {
    padding: 12px;
    border-bottom: 1px solid #cccccc;
  }

  /* Column dividers (adds border to all but the last column) */
  th:not(:last-child), td:not(:last-child) {
    border-right: 1px solid #cccccc;
  }

  /* Removes the bottom border from the very last row */
  tr:last-child td {
    border-bottom: none;
  }
</style>
