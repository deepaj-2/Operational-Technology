FROM eclipse-temurin:8-jdk-jammy

ENV TOMCAT_VERSION=9.0.118
ENV CATALINA_HOME=/opt/tomcat
ENV PATH="${CATALINA_HOME}/bin:${PATH}"

RUN apt-get update && apt-get install -y ca-certificates curl tar && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL "https://archive.apache.org/dist/tomcat/tomcat-9/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz" -o /tmp/tomcat.tar.gz && mkdir -p /opt && tar -xzf /tmp/tomcat.tar.gz -C /opt && mv "/opt/apache-tomcat-${TOMCAT_VERSION}" "${CATALINA_HOME}" && rm /tmp/tomcat.tar.gz

RUN rm -rf ${CATALINA_HOME}/webapps/docs ${CATALINA_HOME}/webapps/examples ${CATALINA_HOME}/webapps/host-manager ${CATALINA_HOME}/webapps/manager

RUN curl -fsSL "https://github.com/ScadaBR/ScadaBR/releases/download/v1.2/ScadaBR.war" -o ${CATALINA_HOME}/webapps/ScadaBR.war

EXPOSE 8080

CMD ["catalina.sh", "run"]