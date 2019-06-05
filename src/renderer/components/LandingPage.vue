<template>
  <el-container style="height: 500px; border: 1px solid #eee">
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu :default-openeds="['1', '3']">
      <el-submenu index="1">
       <el-menu-item index="1-1">选项1</el-menu-item>
         <el-menu-item index="1-1">
           <router-link to="analyse">
                关联规则挖掘
           </router-link></el-menu-item>
      </el-submenu>

    </el-menu>
  </el-aside>

  <el-container>
    <el-header style="text-align: right; font-size: 12px">
    </el-header>
    <el-main>
      <router-view></router-view>

    </el-main>
  </el-container>
</el-container>
</template>

<script>
   export default {
     provide () {
       return {
         reload: this.reload
       }
     },
     reload () {
       this.alive = false
       this.$nextTick(() => {
         this.alive = true
       })
     },
     data () {
       return {

       }
     }
   }
</script>

<style>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }

  .el-aside {
    color: #333;
  }
</style>