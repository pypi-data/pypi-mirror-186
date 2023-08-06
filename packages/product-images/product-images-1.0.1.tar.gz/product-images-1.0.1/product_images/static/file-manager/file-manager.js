
FileManager = function (params) {
    var $select = params.$select,
        $container = $('[data-role=images-container]'),
        $dropLinkSection = $container.find('[data-role=drop-link-section]'),
        $dropFilesSection = $container.find('[data-role=drop-files-section]'),
        $files = $container.find('[data-role=files]'),
        removeMessage = params.removeMessage,
        html = $('html');

    renderFiles(params.initial || []);

    new Dropzone($dropFilesSection[0], {
        url: params.uploadUrl,
        createImageThumbnails: false,
        acceptedFiles: 'image/*',
        parallelUploads: 5,
        addedfile: function(file) {},
        success: function (file, response) {
            renderFile(response);
        },
        error: function (file, response) {
            console.log(response);
        }
    });

    $files.sortable({
        items:'.file-preview',
        cursor: 'move',
        opacity: 0.7,
        distance: 20,
        tolerance: 'pointer',
        update: function(event, ui) {
            $select.empty();
            $files.find('.file-preview').each(function () {
                addOption($(this).data('file-id'));
            });
        }
    });

    function renderFiles(files) {
        $select.empty();

        $.each(files, function () {
            renderFile(this);
        });
    }

    function renderFile(file) {
        var $file = $('<div />').addClass('file-preview').data('file-id', file.id),
            $img = $('<img />').prop('src', file.url),
            $removeBtn = $('<button type="button" />').addClass('remove-btn');

        addOption(file.id);

        $file.append($img);
        $file.append($removeBtn);

        $files.append($file);

        $removeBtn.click(function (e) {
            if (confirm(removeMessage)) {
                $.post(file.remove_url);
                $select.find('option[value=' + file.id + ']').remove();
                $file.remove();
            }
        });
    }

    function addOption(fileId) {
        var $option = $('<option />').prop({
                value: fileId,
                selected: true
            }).text(fileId);

        $select.append($option);
    }

    function handleLinkSectionDrop(event) {
        var html,
            url,
            data;

        stopEvent(event);

        html = event.originalEvent.dataTransfer.getData('text/html');
        url = $('<div />').html(html).find("img").attr('src');
        data = {url: url};

        $.post(
            params.uploadUrl,
            data
        ).success(function (response) {
            renderFile(response);
        }).fail(function (response) {
            console.log(response);
        });
    }

    function stopEvent(event) {
        event.preventDefault();
        event.stopPropagation();
    }

    html.on('dragover', stopEvent);
    html.on('dragleave', stopEvent);

    $dropLinkSection.on('drop', handleLinkSectionDrop);

};
