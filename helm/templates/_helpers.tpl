{{- define "portfolio.labels" -}}
app: {{ .Release.Name }}
chart: {{ .Chart.Name }}-{{ .Chart.Version }}
managed-by: Helm
{{- end -}}
