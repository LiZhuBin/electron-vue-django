<template>
    <div>
        <el-table
                :data="this.tableData"
                height="300"
                border
                style="width: 100%" >
            <el-table-column
                    v-for="{ prop, label } in colConfigs"
                    :key="prop"
                    :prop="prop"
                    :label="label">

            </el-table-column>

        </el-table>
        <el-badge></el-badge>
        <div style="text-align:center" slot="header">
            <el-button type="primary" round @click="changeContents" >进行关联规则转化</el-button>

        </div>
    </div>
</template>

<script>
  export default {
    name: 'AprioriPage',
    mounted: function () {
      this.init()
    },
    data () {
      this.colConfigs = [
        { prop: 'index', label: '数据索引' },
        { prop: 'item', label: '一起买的订单编号' }
      ]
      return {
        tableData: []
      }
    },
    methods: {
      init: function () {
        // eslint-disable-next-line no-unused-expressions
        var self = this
        self.$http.get('http://localhost:8000/polls/apriori/getdata').then((response) => {
          this.tableData = response.data
          console.info(response.data)
        }).catch(function (error) {
          console.info(error)
        })
      }
    }
  }
</script>

<style scoped>

</style>