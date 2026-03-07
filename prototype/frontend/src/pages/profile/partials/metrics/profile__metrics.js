function profile__metricsjs() {
    const group2name = {
        "text": "Лингвистические признаки",
        "entities": "Сущностная разметка",
        "pos": "Частеречная разметка",
        "punct": "Пунктуационные признаки"
    }

    function renderMetrics(features) {
        const $groupsContainer = $('#groupsContainer');
        const $groupPrototype = $('#groupPrototype');
        const $metricPrototype = $('#metricPrototype');

        const groups = Object.entries(features).map(([name, groupFeatures]) => {
            const $group = $groupPrototype.clone();
            $group.removeAttr('id');
            $group.removeClass('hidden');
            $group.find('.metrics-group__title').text(group2name[name] || "Неизвестная группа");

            const metrics = Object.entries(groupFeatures).map(([metric, value]) => {
                const $metric = $metricPrototype.clone();
                $metric.removeAttr('id');
                $metric.removeClass('hidden');
                $metric.find('.metric__name').text(metric);
                $metric.find('.metric__value').text(value.toFixed(3));
                return $metric;
            });

            $group.find('.metrics-group__list').append(metrics);

            return $group;
        });

        $groupsContainer.append(groups);

        $groupPrototype.remove();
        $metricPrototype.remove();
    }

    return renderMetrics
}