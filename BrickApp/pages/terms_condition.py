import dash
from dash import html, dcc
import  dash_mantine_components as dmc
from dash_iconify import DashIconify


dash.register_page(__name__, path='/terms&condition')

terms_and_condition_1 = "Users acknowledge and agree that the BrickLLM app is provided “as is,” without warranty of any kind, \
    and that users assume all risks and liabilities arising from or relating to its use of and reliance upon the tool. \
Eurac Research and Politecnico of Turin make no representations or warranties of any kind whatsoever, express or implied, at law or in equity, \
in connection with or with respect to the tool, including any representations or warranties in regard to quality, performance, \
or noninfringement." 
terms_and_condition_2 = "Please note that this tool does not collect or store any of your personal \
      data or information (e.g. API key) or track your usage in any way."

# license = "

lic_1 = "Copyright (c) 2025, Eurac research"
lic_2 = "All rights reserved."
lic_3 = "Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:"
lice_4 = dmc.ListItem("1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.", mt=10)
lice_5 = dmc.ListItem("2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.", mt=10)
lice_6 = dmc.ListItem("3. All advertising materials mentioning features or use of this software must display the following acknowledgement: This product includes software developed by Eurac research and Politecnico of Turin.", mt=10)
lice_7 = dmc.ListItem("4. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.", mt=10)



# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# 3. All advertising materials mentioning features or use of this software must
#    display the following acknowledgement:
#      This product includes software developed by Eurac research and Politecnico of Turin.

# 4. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.

lice_8 = "THIS SOFTWARE IS PROVIDED BY COPYRIGHT HOLDER 'AS IS' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL COPYRIGHT HOLDER BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, \
    PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; \
        OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, \
            WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."


layout_ = dmc.Container(
    mt=90,
    mb=185,
    children= [
        dmc.ScrollArea(
            children = [
                dmc.Center(
                    dmc.Title("Terms & Condition", mt=100, fw=700, order=1),
                ),
                dmc.Text(terms_and_condition_1, size="lg", mt=100),
                dmc.Text(terms_and_condition_2, size="lg", mt=40,  td="underline", fw=700),
                dmc.Center(
                    dmc.Title("License", mt=100, fw=700, order=1),
                ),
                dmc.Title("BSD 4-Clause License", mt=20, fw=700, order=2),
                dmc.Text(lic_1, mt=20),
                dmc.Text(lic_2, mt=20),
                dmc.Text(lic_3, mt=20),
                dmc.List(
                    mt=20,
                    # type="ordered",
                    children = [
                        lice_4,lice_5,lice_6,lice_7
                    ]
                ),
                dmc.Text(lice_8, mt=40)

            ]
        )
    ]
)

def layout():
    return layout_
