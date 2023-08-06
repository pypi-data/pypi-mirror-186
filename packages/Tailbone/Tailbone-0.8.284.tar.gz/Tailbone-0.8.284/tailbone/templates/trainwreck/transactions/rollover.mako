## -*- coding: utf-8; -*-
<%inherit file="/page.mako" />

<%def name="title()">${index_title} &raquo; Yearly Rollover</%def>

<%def name="content_title()">Yearly Rollover</%def>

<%def name="page_content()">
  <br />

  % if six.text_type(next_year) not in trainwreck_engines:
      <b-notification type="is-warning">
        You do not have a database configured for next year (${next_year}).&nbsp;
        You should be sure to configure it before next year rolls around.
      </b-notification>
  % endif

  <p class="block">
    The following Trainwreck databases are configured:
  </p>

  <b-table :data="engines">
    % if buefy_0_8:
    <template slot-scope="props">
    % endif
      <b-table-column field="key"
                      label="DB Key"
                      % if not buefy_0_8:
                      v-slot="props"
                      % endif
                      >
        {{ props.row.key }}
      </b-table-column>
      <b-table-column field="oldest_date"
                      label="Oldest Date"
                      % if not buefy_0_8:
                      v-slot="props"
                      % endif
                      >
        <span v-if="props.row.error" class="has-text-danger">
          error
        </span>
        <span v-if="!props.row.error">
          {{ props.row.oldest_date }}
        </span>
      </b-table-column>
      <b-table-column field="newest_date"
                      label="Newest Date"
                      % if not buefy_0_8:
                      v-slot="props"
                      % endif
                      >
        <span v-if="props.row.error" class="has-text-danger">
          error
        </span>
        <span v-if="!props.row.error">
          {{ props.row.newest_date }}
        </span>
      </b-table-column>
    % if buefy_0_8:
    </template>
    % endif
  </b-table>
</%def>

<%def name="modify_this_page_vars()">
  ${parent.modify_this_page_vars()}
  <script type="text/javascript">

    ThisPageData.engines = ${json.dumps(engines_data)|n}

  </script>
</%def>


${parent.body()}
