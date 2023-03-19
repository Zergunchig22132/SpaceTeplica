var g_data
function get_data(){
  $.ajax({
    url: "/ajax/power_chart",
    cache: false,
    dataType: 'json',
    success: function(data) {
      g_data=data
    }
});
}

function load_power_chart()
{
  chart_date = google.visualization.arrayToDataTable([
    ["На что распределяется", "Сколько"],
    ["Электричество", g_data["electricity_kpd"]],
    ["Двигатель", g_data["engine_kpd"]]
  ]);
  var options = {
    title: 'Распределение мощности реактора'
  };
  var chart = new google.visualization.PieChart(document.getElementById('power_chart'));
  chart.draw(chart_date, options);
  var html = "<h3>"+"Ресурсы в точках"+"</h3>";
      html += '<table class="tbl"><thead><tr><th>День</th><th>SH</th><th>Топливо</th><th>Кислород</th></tr></thead><tbody>';
      for (var i = 1, len = Object.keys(g_data["resources"]).length; i <= len; ++i) {
          html += '<tr>';
          html += '<td>' + (i) + '</td>'
          html += '<td>' + g_data["resources"]['' + i][0] + '</td>'
          html += '<td>' + g_data["resources"]['' + i][1] + '</td>'
          html += '<td>' + g_data["resources"]['' + i][2] + '</td>'
          html += "</tr>";
      }
      html += '</tbody></table>';
      $('#dyn_table').html(html);

  var Ox = g_data["resources"]["1"][1];
  var T = g_data["history"][1][6];
  var SH = g_data["history"][1][2];
  var html2 = '<table><thead><tr><td colspan="2" align="center">АВТОКЛАВ</td></tr></thead><tbody align="center"><tr><td>Кислород</td><td>' + Ox + '</td></tr><tr><td>T</td><td>' + T + '</td></tr><tr><td>SH</td><td>'+ SH +'</td></tr></tbody></table>';
  $('#table').html(html2);
  var day = g_data["days"];
  var html3 = '<p>Дней:</p><p>'+ day +'</p>';
  $('#days').html(html3);
}
