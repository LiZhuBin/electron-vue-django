<template>
    <el-card >
        <el-header>选择日期</el-header>
        <el-badge></el-badge>
        <div class="block" style="text-align:center">
            <span class="demonstration">带快捷选项</span>
            <el-date-picker
                    v-model="value2"
                    type="daterange"
                    align="right"
                    unlink-panels
                    range-separator="至"
                    start-placeholder="开始日期"
                    end-placeholder="结束日期"
                    :picker-options="pickerOptions"
            @change="changeHandler">
            </el-date-picker>
        </div>
    </el-card>
    </template>
<script>
  export default {
    name: "DateSelect",
    data() {
      return {
        pickerOptions: {
          shortcuts: [{
            text: '最近一周',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近一个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近三个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit('pick', [start, end]);
            }
          }]
        },
        value1: '',
        value2: '',
        values: []
      };
    },
    methods:{
      changeHandler(value, itemName) {
       // this.$store.state.date_select = [];

        this.$store.state.date_select = value
      }
    }
  }
</script>

<style scoped>

</style>