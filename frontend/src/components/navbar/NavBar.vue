<script setup>

import Menuicon from "@/components/navbar/icon/Menuicon.vue";
import Homepageicon from "@/components/navbar/icon/Homepageicon.vue";
import Creaticon from "@/components/navbar/icon/Creaticon.vue";
import Friendicon from "@/components/navbar/icon/Friendicon.vue";
import Searchicon from "@/components/navbar/icon/Searchicon.vue";
</script>

<template>
<div class="drawer lg:drawer-open">
  <input id="my-drawer-4" type="checkbox" class="drawer-toggle" />
  <div class="drawer-content">
    <!-- Navbar -->
    <nav class="navbar w-full h-14 bg-base-100 shadow-sm">
      <div class="navbar-start">
              <label for="my-drawer-4" aria-label="open sidebar" class="btn btn-square btn-ghost">
                 <!-- 菜单icon -->
                  <Menuicon/>
              </label>
              <div class="px-2 font-bold text-xl">AIFriends</div>
      </div>
      <div class="navbar-center w-4/5 max-w-180 flex justify-center">
        <div class="join w-4/5 flex justify-center">
          <input class="input join-item rounded-l-full w-4/5" placeholder="搜索你感兴趣的内容" />
          <button class="btn join-item rounded-r-full gap-0">
            <Searchicon/>
            搜索
          </button>
        </div>
      </div>

      <div class="navbar-end">
        <RouterLink :to="{name:'user-account-login-index'}" active-class="btn-active" class="btn btn-neutral btn-outline" text-lg>登录</RouterLink>
      </div>

    </nav>
    <!-- Page content here -->
    <slot>

    </slot>
  </div>

  <div class="drawer-side is-drawer-close:overflow-visible">
    <label for="my-drawer-4" aria-label="close sidebar" class="drawer-overlay"></label>
    <div class="flex min-h-full flex-col items-start bg-base-200 is-drawer-close:w-16 is-drawer-open:w-54">
      <!-- Sidebar content here -->
      <ul class="menu w-full grow">
        <!-- 首页 -->
        <li>
          <RouterLink :to="{name:'homepage-index'}" active-class="menu-focus" class="is-drawer-close:tooltip is-drawer-close:tooltip-right flex h-14 items-center gap-2" data-tip="首页" my1="">
            <!-- 首页icon -->
            <Homepageicon/>
            <!-- whitespace-nowrap禁止换行 -->
            <span class="is-drawer-close:hidden whitespace-nowrap">首页</span>
          </RouterLink>
        </li>

        <!-- 创作 -->
        <li>
          <RouterLink :to="{name:'create-index'}" active-class="menu-focus" class="is-drawer-close:tooltip is-drawer-close:tooltip-right flex h-14 items-center gap-2" data-tip="创作" my1="">
            <!-- 创作icon -->
            <Creaticon/>
            <!-- whitespace-nowrap禁止换行 -->
            <span class="is-drawer-close:hidden whitespace-nowrap">创作</span>
          </RouterLink>
        </li>

         <!-- 好友-->
        <li>
          <RouterLink :to="{name:'friend-index'}" active-class="menu-focus" class="is-drawer-close:tooltip is-drawer-close:tooltip-right flex h-14 items-center gap-2" data-tip="好友" my1="">
            <!-- 好友icon -->
            <Friendicon/>
            <!-- whitespace-nowrap禁止换行 -->
            <span class="is-drawer-close:hidden whitespace-nowrap">好友</span>
          </RouterLink>
        </li>

      </ul>
    </div>
  </div>
</div>
</template>

<style scoped>

</style>
