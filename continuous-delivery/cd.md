# Continuous Delivery

Entrega continua corresponde a una recopilación de muchas de las mejores prácticas ágiles y organizativas exitosas anteriores. CD enfoca a la organización en la construcción de un proceso de deploy de software automatizado y simplificado. El corazón de un de un proceso de release es un loop de feedback iterativo. Este proceso gira en torno a la entrega del software al usuario final lo más rápido posible, aprendiendo de su experiencia práctica para incorporarr el feedback recolectado en el siguiente release.


###### Continuous integration vs. continuous delivery vs. continuous deployment
* __Continuous integration__: Los developers que la practican fusionan sus cambios en la rama principal tan a menudo como sea posible. Los cambios de los desarrolladores son validados creando una compilación y ejecutando pruebas automatizadas contra la aplicación. Al hacerlo, se evitan los errores de integración que suelen ocurrir cuando llega el día del lanzamiento de la nueva versión. La integración continua pone énfasis en probar que la aplicación funcione al integrar los commits a la rama `master`.
    * __Costos__:
        * El equipo tendrá que escribir tests automatizados para cada feature, mejora o bug fix.
        * Servidor de integración continua que monitoree el repositorio principal y corra autimáticamente los tests para cada push.
        * Los desarroladores necesitan hacer merge de sus cambios tan a menudo como sea posible.
    * __Beneficios__:
        * Se envían menos errores a producción.
        * Crear un release es fácil ya que todos los problemas de integración se han resuelto.
        * Menos cambio de contexto ya que los developers son alertados a penas gatillan un error en la compilación o las pruebas y así pueden trabajar en solucionarlo antes de pasar a otro ticket.
        * Costos de testing son reducidos drásticamente ya que el CI server puede ejecutar cientos de pruebas en segundos.

* __Continuous delivery__: Entrega continua es una extensión de la integración continua para asegurarse de que puede lanzar nuevos cambios a los clientes de forma rápida y sostenible. Esto significa que además de haber automatizado las pruebas, también se ha automatizado su proceso de release y puedes hacer deploy de la cualquier versión de la aplicación en cualquier momento con un click. Si se desean obtener beneficios de la entrega continua se debe hacer deploy en producción lo antes posible para asegurarse de que libera pequeños pedazos de la aplicación que son fáciles de resolver en caso de que surja algún inconveniente.
    * __Costos__:
        * Base sólida en la integración continua y la suite de test necesita cubrir lo suficiente del proyecto.
        * Deploys necesitan ser automatizados. El trigger es todavía manual pero una vez que se inicia el deploy no debería ser necesaria la interveción humana.
        * Es muy probable que su equipo deba adoptar indicadores de features para que las funciones incompletas no afecten a los users en producción.
    * __Beneficios__:
        * Se elimina la complejidad del deploy de la app.
        * Se pueden publicar nuevas versiones de la app con mayor frecuencia, acelarando así el ciclo de feedback del cliente.
        * Hay mucha menos presión sobre las decisiones para pequeños cambios, por lo que se fomenta la iteración más rápida.

* __Continuous deployment__: Con esta práctica, cualquier cambio que pase todas las etapas del pipeline de producción es publicado a los usuarios. No hay interveción humana y sólo un test fallido evitará que se implemente el cambio en producción.
    * __Costos__:
        * Se debe tener una buena cultura de pruebas. La calidad de la suite de test determinará la calidad de los deployments.
        * El proceso de documentación debe mantenerse al día con los deployments.
        * Los indicadores de los features se convierten en una parte inherente del proceso de deployment de cambios significativos para asegurarse de que pueda coordinar con otros departamentos (Soporte, Marketing, Relaciones Públicas).
    * __Beneficios__:
        * No es necesario detenerse el momento de tener un nuevo release. Los deployments son gatillados automáticamente con cada cambio.
        * Las versiones son menos riesgosas y más fáciles de solucionar en caso de que surja un problema al implementar pequeños cambios.
        * Los clientes ven un flujo continuo de mejoras, y la calidad aumenta cada día, en lugar de cada mes, trimestre o año.

En síntesis, continuous integration es parte de continuous delivery y  continuous deployment. Y continuous deployment es como continuous delivery, excepto que las versiones se producen automáticamente.

![](img/1.png)
