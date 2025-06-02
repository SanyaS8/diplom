<script setup>

</script>

<template>
<div class="profile-title">
  <slot />
</div>
</template>

<style scoped>
.profile-title {
  background: url("/train.png");
  padding: 30px;
  border-radius: 15px;
  font-size: 42px;
  font-weight: bold;
  color: #fff;
  background-size: 100%;
  height: 200px;
  background-position: center;
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}
</style>