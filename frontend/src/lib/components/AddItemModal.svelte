<script lang="ts">
  let { showModal = $bindable() } = $props();
</script>

{#if showModal}
  <div class="overlay">
    <div class="modal-panel">
      <div class="modal-header">
        Add a New Item
        <hr />
      </div>
      <div class="modal-body">
        <label for="url">Product URL</label>
        <br />
        <input type="text" id="url" placeholder="https://example.com" />
        <hr />
      </div>
      <div class="modal-footer">
        <button onclick={() => (showModal = false)}>Cancel</button>
        <button>Add</button>
      </div>
    </div>
  </div>
{/if}

<style>
  hr {
    margin-top: 6px;
    margin-bottom: 0;
  }
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.7);
    z-index: 999;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .modal-panel {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    width: 90%;
    max-width: 500px;
  }
  .modal-header {
    padding: 24px 16px 0 16px;
    font-size: 1.5em;
    font-weight: bold;
  }
  .modal-body {
    padding: 8px 16px;
  }
  .modal-footer {
    padding: 0 16px 24px 16px;
    display: flex;
    justify-content: flex-end;
    gap: 10px;
  }
</style>
