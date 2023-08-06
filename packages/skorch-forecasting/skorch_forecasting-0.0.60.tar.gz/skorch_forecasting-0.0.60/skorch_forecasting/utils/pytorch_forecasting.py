def output_class(net=None, **res):
    """Auxiliary for pytorch-forecasting modules output
    pytorch-forecasting require an output_class method that gets called at the
    end of every forward pass and deals with all the output information from
    the model. Since skorch only requires the actual prediction to compute the
    loss, that is the only thing we extract.

    Notes
    -----
    Notice this is not actually a class. The name follows from the private
    attribute ``_output_class`` (which is where this function is assigned to)
    in all pytorch_forecasting models.

    Parameters
    ----------
    net : pytorch-forecasting model
        Compatability purposes (equivalent to self)
    **res : dict
        Dictionary containing info about the results
    Returns
    -------
    predictions : torch.tensor
    """
    return res['prediction'].squeeze(-1)


def output_transformer(module, out=None):
    """Auxiliary for pytorch-forecasting modules output
    pytorch-forecasting modules require a pickable callable that takes network
    output and transforms it to prediction space. Since for our purpose,
    predictions already are in the prediction space (we inverse transform
    predictions after training using sklearn), we leave them untouched.

    Parameters
    ----------
    module : pytorch-forecasting model
        Compatability purposes (equivalent to self)
    out : dict
        Dictionary containing info about the results
    Returns
    -------
    predictions : torch.tensor
    """
    if isinstance(module, dict):
        return module['prediction']
    return out['prediction']
