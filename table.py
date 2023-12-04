table_head = """
                    <table border=1 class=comm_table2 width=100%>
                        <tbody>
                            <tr>
                                <td colspan=4 style=background-color:#015293;color:#fff;line-height:40px><span
                                        id=cycs>查验次数：第{}次</span>
                                    <span style=padding-left:50px id=cysj>查验时间：{}</span>
                                    <span style=float:right>
                                </td>
                            </tr>
                    </table>
"""
table_head_string = """
                                            <table cellspacing=0 cellpadding=0 style=width:100% class=fppy_table_box>
                                                <tbody>
                                                    <tr id=tab_head_dzfp>
                                                        <td class="align_center borderRight" width=30%>货物或应税劳务、服务名称</td>
                                                        <td class="align_center borderRight" width=10%>规格型号</td>
                                                        <td class="align_center borderRight" width=5%>单位</td>
                                                        <td class="align_center borderRight" width=10%>数量</td>
                                                        <td class="align_center borderRight" width=10%>单价</td>
                                                        <td class="align_center borderRight" width=15%>金额</td>
                                                        <td class="align_center borderRight" width=5%>税率</td>
                                                        <td class=align_center width=15%>税额</td>
"""
table_content_string="""
                                                    <tr>
                                                        <td class="align_left borderRight"><span
                                                                class=content_td_blue>*电信服务*通信服务费</span>
                                                        <td class="align_left borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_left borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue>108.30</span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue>0%</span>
                                                        <td class=align_right><span class=content_td_blue>0.00</span>
                                                    </tr>

"""
heji_table="""
                                                    <tr>
                                                        <td class="align_center borderRight">合计</td>
                                                        <td class="align_center borderRight">&nbsp;</td>
                                                        <td class="align_center borderRight">&nbsp;</td>
                                                        <td class="align_center borderRight">&nbsp;</td>
                                                        <td class="align_center borderRight">&nbsp;</td>
                                                        <td class="align_right borderRight"><span class=content_td_blue
                                                                id=je_dzfp>￥{}</span></td>
                                                        <td class="align_center borderRight">&nbsp;</td>
                                                        <td class=align_right><span class=content_td_blue
                                                                id=se_dzfp>￥{}</span></td>
                                                    </tr>
                                                    <tr>
                                                        <td class="align_center borderRight borderTop">价税合计（大写）</td>
                                                        <td colspan=4 class="align_left borderTop"><span
                                                                class=align_left><span class=content_td_blue
                                                                    id=jshjdx_dzfp>⊗{}</span></span></td>
                                                        <td colspan=3 class="align_left borderTop"><span
                                                                style="padding:0 20px">（小写）</span><span
                                                                class=content_td_blue id=jshjxx_dzfp>￥{}</span></td>
                                                    </tr>
                                            </table>
"""