## -*- coding: utf-8; -*-
<%inherit file="/page.mako" />

<%def name="title()">TempMon Appliances &raquo; Dashboard</%def>

<%def name="content_title()">Dashboard</%def>

<%def name="extra_javascript()">
  ${parent.extra_javascript()}
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.bundle.min.js"></script>
  % if not use_buefy:
  <script type="text/javascript">

    var contexts = {};
    var charts = {};

    function fetchReadings(appliance_uuid) {
        if (appliance_uuid === undefined) {
            appliance_uuid = $('#appliance_uuid').val();
        }

        $('.form-wrapper').mask("Fetching data");

        if (Object.keys(charts).length) {
            Object.keys(charts).forEach(function(key) {
                charts[key].destroy();
                delete charts[key];
            });
        }

        var url = '${url("tempmon.dashboard.readings")}';
        var params = {'appliance_uuid': appliance_uuid};
        $.get(url, params, function(data) {

            if (data.probes) {
                data.probes.forEach(function(probe) {
                    charts[probe.uuid] = new Chart(contexts[probe.uuid], {
                        type: 'scatter',
                        data: {
                            datasets: [{
                                label: probe.description,
                                data: probe.readings
                            }]
                        },
                        options: {
                            scales: {
                                xAxes: [{
                                    type: 'time',
                                    time: {unit: 'minute'},
                                    position: 'bottom'
                                }]
                            }
                        }
                    });
                });
            } else {
                // TODO: should improve this
                alert(data.error);
            }

            $('.form-wrapper').unmask();
        });
    }

    $(function() {

        % for probe in appliance.probes:
            contexts['${probe.uuid}'] = $('#tempchart-${probe.uuid}');
        % endfor

        $('#appliance_uuid').selectmenu({
            change: function(event, ui) {
                $('.form-wrapper').mask("Fetching data");
                $(this).parents('form').submit();
            }
        });

        fetchReadings();
    });

  </script>
  % endif
</%def>

<%def name="render_this_page()">
  % if use_buefy:

      ${h.form(request.current_route_url(), ref='applianceForm')}
      ${h.csrf_token(request)}
      <div class="level-left">

        <div class="level-item">
          <b-field label="Appliance" horizontal>
            <b-select name="appliance_uuid"
                      v-model="applianceUUID"
                      @input="$refs.applianceForm.submit()">
              <option v-for="appliance in appliances"
                      :key="appliance.uuid"
                      :value="appliance.uuid">
                {{ appliance.name }}
              </option>
            </b-select>
          </b-field>
        </div>

        % if appliance:
            <div class="level-item">
              <a href="${url('tempmon.appliances.view', uuid=appliance.uuid)}">
                ${h.image(url('tempmon.appliances.thumbnail', uuid=appliance.uuid), "")}
              </a>
            </div>
        % endif

      </div>
      ${h.end_form()}

      % if appliance and appliance.probes:
          % for probe in appliance.probes:
              <h4 class="is-size-4">
                Probe:&nbsp; ${h.link_to(probe.description, url('tempmon.probes.graph', uuid=probe.uuid))}
                (status: ${enum.TEMPMON_PROBE_STATUS[probe.status]})
              </h4>
              % if probe.enabled:
                  <canvas ref="tempchart-${probe.uuid}" width="400" height="60"></canvas>
              % else:
                  <p>This probe is not enabled.</p>
              % endif
          % endfor
      % elif appliance:
          <h3>This appliance has no probes configured!</h3>
      % else:
          <h3>Please choose an appliance.</h3>
      % endif

  % else:
  ## not buefy
  <div style="display: flex;">

    <div class="form-wrapper">
      <div class="form">
        ${h.form(request.current_route_url())}
        ${h.csrf_token(request)}
        % if use_buefy:
            <b-field horizontal label="Appliance">
              ${appliance_select}
            </b-field>
        % else:
            <div class="field-wrapper">
              <label>Appliance</label>
              <div class="field">
                ${appliance_select}
              </div>
            </div>
        % endif
        ${h.end_form()}
      </div>
    </div>

    <a href="${url('tempmon.appliances.view', uuid=appliance.uuid)}">
      ${h.image(url('tempmon.appliances.thumbnail', uuid=appliance.uuid), "")}
    </a>
  </div>

  % if appliance.probes:
      % for probe in appliance.probes:
          <h3>
            Probe:&nbsp; ${h.link_to(probe.description, url('tempmon.probes.graph', uuid=probe.uuid))}
            (status: ${enum.TEMPMON_PROBE_STATUS[probe.status]})
          </h3>
          % if probe.enabled:
              % if use_buefy:
                  <canvas ref="tempchart" width="400" height="150"></canvas>
              % else:
                  <canvas id="tempchart-${probe.uuid}" width="400" height="60"></canvas>
              % endif
          % else:
              <p>This probe is not enabled.</p>
          % endif
      % endfor
  % else:
      <h3>This appliance has no probes configured!</h3>
  % endif
  % endif
</%def>

<%def name="modify_this_page_vars()">
  ${parent.modify_this_page_vars()}
  <script type="text/javascript">

    ThisPageData.appliances = ${json.dumps(appliances_data)|n}
    ThisPageData.applianceUUID = ${json.dumps(appliance.uuid if appliance else None)|n}
    ThisPageData.charts = {}

    ThisPage.methods.fetchReadings = function(uuid) {

        if (!uuid) {
            uuid = this.applianceUUID
        }

        for (let chart in this.charts) {
            chart.destroy()
        }
        this.charts = []

        let url = '${url('tempmon.dashboard.readings')}'
        let params = {appliance_uuid: uuid}
        this.$http.get(url, {params: params}).then(response => {
            if (response.data.probes) {

                for (let probe of response.data.probes) {

                    let context = this.$refs[`tempchart-${'$'}{probe.uuid}`]
                    this.charts[probe.uuid] = new Chart(context, {
                        type: 'scatter',
                        data: {
                            datasets: [{
                                label: probe.description,
                                data: probe.readings
                            }]
                        },
                        options: {
                            scales: {
                                xAxes: [{
                                    type: 'time',
                                    time: {unit: 'minute'},
                                    position: 'bottom'
                                }]
                            }
                        }
                    })
                }

            } else {
                alert(response.data.error)
            }
        })
    }

    ThisPage.mounted = function() {
        this.fetchReadings()
    }

  </script>
</%def>


${parent.body()}
