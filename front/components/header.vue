<template>
  <a-layout-header>
    <div class="logo">twdouga</div>
    <a-menu
      theme="dark"
      mode="horizontal"
      :default-selected-keys="[$route.path]"
      :style="{ lineHeight: '64px' }"
    >
      <a-menu-item key="/">
        <NuxtLink to="/">動画保存</NuxtLink>
      </a-menu-item>
      <a-menu-item key="/list">
        <NuxtLink to="/list">注目動画</NuxtLink>
      </a-menu-item>
    </a-menu>
  </a-layout-header>
</template>
